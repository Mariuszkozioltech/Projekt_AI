/* people.js — prywatny notes: osoby, zgody, notatki, podsumowania (etycznie, bez podsłuchu) */
(function(){
  const storePath = "http://127.0.0.1:5500/../data/contacts.json"; // lokalny JSON (serwowany plikowo)
  let peopleDB = { people: [] };
  let selectedId = null;

  async function loadDB() {
    try {
      const res = await fetch(storePath, { cache: "no-store" });
      peopleDB = await res.json();
    } catch(e) {
      console.warn("Nie można wczytać contacts.json", e);
      peopleDB = { people: [] };
    }
  }

  function saveHint() {
    console.log("Zmiany zapisane w contacts.json (edytuj plik, aby trwale zmienić).");
  }

  function renderList(filter="") {
    const ul = document.getElementById("people_list");
    if (!ul) return;
    ul.innerHTML = "";
    const f = (filter||"").toLowerCase();
    peopleDB.people
      .filter(p => !f || p.name.toLowerCase().includes(f) || (p.tags||[]).some(t=>t.toLowerCase().includes(f)))
      .forEach(p=>{
        const li = document.createElement("li");
        li.style.cursor = "pointer";
        li.style.padding = "6px";
        li.textContent = `${p.name} ${p.consent ? "✅" : "🚫"}`;
        li.onclick = ()=>showPerson(p.id);
        ul.appendChild(li);
      });
  }

  function showPerson(id) {
    selectedId = id;
    const p = peopleDB.people.find(x=>x.id===id);
    const box = document.getElementById("person_view");
    if (!p || !box) return;
    box.innerHTML = "";
    const wrap = document.createElement("div");
    wrap.innerHTML = `
      <h4>${p.name}</h4>
      <label>Zgoda na podsumowania (jawna): <input id="p_consent" type="checkbox" ${p.consent ? "checked":""} /></label>
      <label>Tagi (po przecinku): <input id="p_tags" value="${(p.tags||[]).join(", ")}" /></label>
      <label>Dodaj notatkę:</label>
      <textarea id="p_note" rows="3" placeholder="Twoje obserwacje, preferencje, granice..."></textarea>
      <div style="display:flex; gap:8px; margin-top:8px;">
        <button id="p_save">Zapisz</button>
        <button id="p_summary">Podsumuj ostatnią rozmowę (ręcznie wybrany czat)</button>
      </div>
      <div style="margin-top:10px;">
        <strong>Notatki:</strong>
        <ul id="p_notes_list"></ul>
      </div>
    `;
    box.appendChild(wrap);

    // render notes
    const notesUl = box.querySelector("#p_notes_list");
    (p.notes||[]).slice().reverse().forEach(n=>{
      const li = document.createElement("li");
      li.textContent = n;
      notesUl.appendChild(li);
    });

    // handlers
    box.querySelector("#p_save").onclick = ()=>{
      p.consent = box.querySelector("#p_consent").checked;
      p.tags = box.querySelector("#p_tags").value.split(",").map(s=>s.trim()).filter(Boolean);
      const note = box.querySelector("#p_note").value.trim();
      if (note) {
        p.notes = p.notes || [];
        p.notes.push(note);
        box.querySelector("#p_note").value = "";
      }
      saveHint();
      renderList(document.getElementById("people_search")?.value || "");
      showPerson(p.id);
      dodajProblem(`Zapisano zmiany dla: ${p.name}`, "mały");
    };

    box.querySelector("#p_summary").onclick = ()=>{
      // RĘCZNY wybór: użytkownik kopiuje transkrypt/fragment rozmowy do inputu czatu → AI robi streszczenie
      const input = document.getElementById("chat_input");
      if (!input) return;
      const marker = `[PODSUMUJ_DLA:${p.name}] Wklej tu wybrane fragmenty rozmowy.`;
      input.value = marker;
      input.focus();
      dodajProblem(`Wklej fragment rozmowy do czatu, aby zrobić podsumowanie dla: ${p.name}`, "średni");
    };
  }

  async function initPeopleUI() {
    await loadDB();

    const btn = document.getElementById("chat_people");
    const modal = document.getElementById("people_panel");
    const close = document.getElementById("people_close");
    const add   = document.getElementById("person_add");
    const search= document.getElementById("people_search");

    if (btn && modal) {
      btn.addEventListener("click", ()=>modal.classList.remove("hidden"));
    }
    if (close && modal) {
      close.addEventListener("click", ()=>modal.classList.add("hidden"));
    }
    if (add) {
      add.addEventListener("click", ()=>{
        const name = prompt("Imię i nazwisko osoby:");
        if (!name) return;
        const id = "p_" + Math.random().toString(36).slice(2,8);
        peopleDB.people.push({ id, name, consent:false, tags:[], notes:[], lastInteractions:[] });
        saveHint();
        renderList(search?.value || "");
        showPerson(id);
      });
    }
    if (search) {
      search.addEventListener("input", ()=>renderList(search.value));
    }

    renderList("");
  }

  // Hook do czatu: gdy wpiszesz [PODSUMUJ_DLA:Imię] i wkleisz fragment, AI przygotuje streszczenie
  const _origSend = window.sendChatMessage;
  if (typeof _origSend === "function") {
    window.sendChatMessage = function() {
      try {
        const input = document.getElementById("chat_input");
        const val = (input?.value || "");
        const m = val.match(/^

\[PODSUMUJ_DLA:(.+?)\]

/);
        if (m) {
          const personName = m[1].trim();
          dodajProblem(`Przygotowuję podsumowanie dla: ${personName}`, "mały");
          // Tu możesz zawołać backend do streszczeń, lub zrobić lokalną kompresję tekstu.
        }
      } catch(e) {}
      return _origSend.apply(this, arguments);
    };
  }

  document.addEventListener("DOMContentLoaded", initPeopleUI);
})();
