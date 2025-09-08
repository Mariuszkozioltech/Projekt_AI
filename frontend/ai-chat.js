function zapiszRozmowe(chatHistory) {
  const teraz = new Date();
  const timestamp = teraz.toISOString().replace(/[:.]/g, "-");
  const linie = chatHistory.map(msg => `${msg.autor}: ${msg.tekst}`).join("\n");
  const blob = new Blob([linie], { type: "text/markdown" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = `${timestamp}_chat.md`;
  link.click();
}

function ocenOdpowiedz(tekst, temat) {
  const wazne = ["pieniądze", "spotkanie", "wyjazd", "decyzja", "termin"];
  if (wazne.includes(temat.toLowerCase())) {
    if (tekst.toLowerCase().includes("brak")) return "❓ Potrzebuję więcej danych.";
    if (tekst.toLowerCase().includes("na podstawie")) return "✅ Potwierdzam na podstawie danych.";
    return "⚠️ Nie jestem pewien, ale oto co wiem...";
  }
  return "";
}
