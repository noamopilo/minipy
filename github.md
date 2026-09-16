# 🚀 Snelcursus: Minipy Pushen naar GitHub

Volg deze stappen in je terminal om je wijzigingen (zoals de nieuwe README en mappenstructuur) live te zetten.

---

## 📂 Stap 1: Zorg dat je in de juiste map staat
Git werkt alleen als je terminal in de hoofdmap van je project staat.
```bash
cd C:\Users\noeba\Desktop\programation\python\minipy
```

## 📝 Stap 2: Controleer je status (Optioneel)
Kijk welke bestanden er zijn aangepast of toegevoegd.
```bash
git status
```
*(Als het goed is, zie je nu je gewijzigde README.md en je nieuwe afbeeldingen in het rood staan).*

## ➕ Stap 3: Voeg de bestanden toe aan de wachtrij
Zet alle nieuwe en gewijzigde bestanden klaar voor de back-up.
```bash
git add .
```

## 💾 Stap 4: Maak de Commit (De vastlegging)
Geef je pakketje een duidelijke naam zodat je weet wat je hebt gedaan.
```bash
git commit -m "docs: finalize professional README and package release"
```

## ☁️ Stap 5: Push naar GitHub!
Stuur alles definitief naar de cloud.
```bash
git push origin main
```

---

## 🔒 Wat als GitHub weigert? (Force Push)
Omdat we de mappenstructuur hebben omgegooid, kan het zijn dat GitHub de geschiedenis niet begrijpt en een `[rejected]` foutmelding geeft. Mocht dat gebeuren, dwing de push dan met deze code:
```bash
git push origin main --force
```
