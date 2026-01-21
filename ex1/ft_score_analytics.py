import sys

argumente = sys.argv[1:]

print("=== PixelMetrics 3000 - Score Cruncher ===\n")

# Prüfe ob Argumente vorhanden sind
if len(argumente) == 0:
    print("❌ Keine Scores eingegeben!")
    print("💡 Nutze:  python3 schritt4_stats.py 100 200 300")
    sys.exit()

# Sammle gültige Scores
scores = []
for arg in argumente:
    try:
        if int(arg) < 0:
            print(f"⚠️  '{arg}' ignoring (negative number)")
            continue
        if arg[1:].isdigit() and arg[0] == '0':
            print(f"⚠️  '{arg}' invalid number")
            continue
        zahl = int(arg)
        scores.append(zahl)
    except ValueError:
        print(f"⚠️  '{arg}' ignoriert (keine Zahl)")

# Prüfe ob gültige Scores vorhanden sind
if len(scores) == 0:
    print("❌ Keine gültigen Scores gefunden!")
    sys.exit()

# Berechne Statistiken
anzahl = len(scores)
hoechster_score = max(scores)
niedrigster_score = min(scores)
summe = sum(scores)
durchschnitt = summe / anzahl
low_scores = [s for s in scores if s < durchschnitt]
high_scores = [s for s in scores if s >= durchschnitt]
score_range = hoechster_score - niedrigster_score

# Ausgabe
print("\n📊 STATISTIKEN")
print("=" * 40)
print(f"Anzahl Scores:       {anzahl}")
print(f"Höchster Score:     {hoechster_score} 🏆")
print(f"Niedrigster Score:  {niedrigster_score}")
print(f"Gesamtsumme:        {summe}")
print(f"Durchschnitt:       {durchschnitt:.2f}")
print(f"Score Range:        {score_range}")
print(f"Low Scores: {len(low_scores)}")
print(f"High Scores: {len(high_scores)}")
print("=" * 40)
print("\n✅ Analyse abgeschlossen. Viel Erfolg beim nächsten Mal!")
