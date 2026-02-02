import sys

argumente = sys.argv[1:]

print("=== PixelMetrics 3000 - Score Cruncher ===\n")

if len(argumente) == 0:
    print("❌ No scores entered!")
    print("💡 Use:  python3 schritt4_stats.py 100 200 300")
    sys.exit()

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
        print(f"⚠️  '{arg}' ignored (not a number)")

# Check if valid scores are present
if len(scores) == 0:
    print("❌ No valid scores found!")
    sys.exit()

# Calculate statistics
count = len(scores)
highest_score = max(scores)
lowest_score = min(scores)
total_sum = sum(scores)
average = total_sum / count
low_scores = [s for s in scores if s < average]
high_scores = [s for s in scores if s >= average]
score_range = highest_score - lowest_score

# Output results
print("\n📊 STATISTICS")
print("=" * 40)
print(f"Number of Scores:       {count}")
print(f"Highest Score:     {highest_score} 🏆")
print(f"Lowest Score:  {lowest_score}")
print(f"Total Sum:        {total_sum}")
print(f"Average:       {average:.2f}")
print(f"Score Range:        {score_range}")
print(f"Low Scores: {len(low_scores)}")
print(f"High Scores: {len(high_scores)}")
print("=" * 40)
print("\n✅ Analysis complete. Good luck next time!")
