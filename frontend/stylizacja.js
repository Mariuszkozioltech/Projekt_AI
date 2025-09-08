/* stylizacja.js — dopasowanie stylu wypowiedzi (ton, tempo, „ludzkie” brzmienie) */
export function detectTone(text) {
  const lower = (text||"").toLowerCase();
  if (lower.includes("?")) return "pytające";
  if (lower.includes("!")) return "emocjonalne";
  return "neutralne";
}
export function applyHumanStyle(text, tone="neutralne") {
  if (!text) return "";
  let t = text.trim();
  if (tone === "emocjonalne") t = t.replace(/\.$/, "!");
  if (tone === "pytające" && !t.endsWith("?")) t += "?";
  // lekkie „oddechy”
  return t;
}
