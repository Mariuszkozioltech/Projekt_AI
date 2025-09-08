window.youtubeConnector = (function(){
  let settings = {
    apiKey: null
  };

  function setApiKey(key) { settings.apiKey = (key||"").trim() || null; }

  // Prosta ekstrakcja ID wideo (yt.be / watch?v=)
  function extractVideoId(url){
    try {
      const u = new URL(url);
      if (u.hostname.includes("youtu.be")) return u.pathname.slice(1);
      if (u.searchParams.get("v")) return u.searchParams.get("v");
      return null;
    } catch { return null; }
  }

  // Tzw. „analiza publiczna”: tu symulujemy pobranie metadanych i komentarzy (API opcjonalne).
  async function analyzePublic(url){
    const videoId = extractVideoId(url);
    const result = { url, type: videoId ? "video" : "channel_or_page", summary: "", flags: [] };

    // Ostrzeżenie o źródle (integracja z Twoją funkcją sprawdzZrodlo)
    try {
      if (typeof sprawdzZrodlo === "function") {
        const info = await sprawdzZrodlo(url);
        if (info?.status && info.status !== "aktywne") {
          result.flags.push("źródło:" + info.status);
        }
      }
    } catch {}

    // Bez API: zróbmy tylko bazowe streszczenie (heurystyki)
    if (!settings.apiKey) {
      result.summary = "Analiza publiczna (bez API): sprawdź tytuł/opis/komentarze ręcznie. Dodano flagi źródła, jeśli niepewne.";
      return result;
    }

    // Z API (szkic – do realnego użycia dodaj fetch do YouTube Data API v3)
    try {
      // Tu możesz dobudować: videos.list, commentThreads.list – używając settings.apiKey
      result.summary = "Analiza publiczna z API: (szkic) – pobierz metadane i komentarze przez YouTube Data API v3.";
    } catch(e){
      result.summary = "Błąd podczas zapytania do API YouTube (sprawdź klucz API).";
      result.flags.push("api_error");
    }
    return result;
  }

  return {
    setApiKey, analyzePublic
  };
})();
