# 🎄 Advent of Code 2025

Welcome to my Advent of Code 2025 solutions repository! This repo contains automated tooling and solutions for all 12 days of coding challenges.

## 📁 Repository Structure

```
advent-of-code-2025/
├── README.md                 # This file
├── generate_day.py          # Smart day generator script
├── auto_generate.sh         # Cron job wrapper script
├── auto_generate.log        # Automated generation logs
├── CRON_SETUP.md           # Cron job setup instructions
├── .gitignore              # Git ignore rules
└── day-X/                  # Daily challenge folders
    ├── solution.py         # Python solution (Part 1)
    ├── solution-part2.py   # Python solution (Part 2)
    ├── solution.rs         # Rust solution (Part 1)
    ├── solution-part2.rs   # Rust solution (Part 2)
    └── solution.csv        # Puzzle input data (gitignored)
```

## 🚀 Quick Start

### Generate Today's Files
```bash
python3 generate_day.py
```

### Generate Specific Day
```bash
python3 generate_day.py 15
```

### Update README Automation
```bash
# Fetch puzzle info and add Daily Log entry
python3 update_readme.py auto <day>

# Mark day as complete in Progress Tracker
python3 update_readme.py complete <day> <part>

# Manually add Daily Log entry
python3 update_readme.py add <day>
```

### Set Up Auto-Generation
```bash
# See CRON_SETUP.md for full instructions
crontab -e
# Add: 0 6 * 12 * /path/to/auto_generate.sh
```

## 🛠️ Features

- **📅 Date-Aware**: Automatically detects which day should be generated
- **⏰ Release Schedule**: Respects AoC release times (06:00 SAST)
- **🔄 Auto-Generation**: Cron job creates files when puzzles are released
- **🐍 🦀 Multi-Language**: Templates for both Python and Rust solutions
- **📝 Smart Logging**: All automation activities are logged
- **🔍 Missing Day Detection**: Finds and creates missing previous days

## 📊 Progress Tracker

### Week 1 (Dec 1-7)
- [x] **Day 1** - ⭐⭐ Dial Puzzle - *Password*
- [x] **Day 2** - ⭐⭐ Gift Shop - *Invalid ID pattern detection*
- [x] **Day 3** - ⭐⭐ Grid Walker - *Navigate through a 2D grid*
- [x] **Day 4** - ⭐⭐ Printing Department - *Navigate printing department challenges*
- [x] **Day 5** - ⭐⭐ Cafeteria - *Solve cafeteria logistics puzzle*
- [x] **Day 6** - ⭐⭐ Trash Compactor - *Cephalopod math worksheet*
- [x] **Day 7** - ⭐⭐ Laboratories - *Laboratory challenges*

### Week 2 (Dec 8-12)
- [x] **Day 8** - ⭐⭐ Playground - *Minimum Spanning Tree in 3D Space*
- [x] **Day 9** - ⭐⭐ Movie Theater - *Largest Rectangle in Polygon*
- [ ] **Day 10** - 📁 Files ready - Available Dec 13 at 06:00 SAST
- [ ] **Day 11** - Available Dec 14 at 06:00 SAST
- [ ] **Day 12** - Final Day! Available Dec 15 at 06:00 SAST ⭐

## 🏃 Running Solutions

### Python Solutions
```bash
cd day-X
python3 solution.py          # Part 1
python3 solution-part2.py    # Part 2
```

### Rust Solutions
```bash
cd day-X
rustc solution.rs && ./solution           # Part 1
rustc solution-part2.rs && ./solution-part2  # Part 2
```

### JavaScript Solutions
```bash
cd day-X
node solution.js             # Part 1
node solution-part2.js       # Part 2
```

## 📝 Daily Log

### Day 1 (Dec 1, 2025)
- **Challenge**: Dial Puzzle - Track position on a circular dial
- **Part 1**: Count how many times the dial reaches position 0
- **Part 2**: [Enhanced version details]
- **Languages**: Python ✅, Rust ✅, JavaScript ✅
- **Time to Solve**: 12 hours 20 minutes
- **Difficulty**: ⭐⭐☆☆☆

### Day 2 (Dec 2, 2025)
- **Challenge**: Gift Shop - Identify invalid product IDs from ranges
- **Part 1**: Find IDs where the number is a pattern repeated exactly twice (e.g., 1212, 565656)
- **Part 2**: Find IDs where the number is any pattern repeated at least twice (e.g., 111, 1212, 123123123)  
- **Languages**: Python ✅, Rust ✅, JavaScript ✅
- **Time to Solve**: 15 minutes
- **Difficulty**: ⭐⭐⭐☆☆

### Day 3 (Dec 3, 2025)
- **Challenge**: Grid Walker
- **Part 1**: Navigate through a 2D grid
- **Part 2**: Completed both parts
- **Languages**: Python ✅, Rust ✅, JavaScript ⏳
- **Time to Solve**: 2 hours 11 minutes
- **Difficulty**: ⭐⭐⭐☆☆

### Day 4 (Dec 4, 2025)
- **Challenge**: Printing Department
- **Part 1**: You ride the escalator down to the printing department. They're clearly getting ready for Christm...
- **Part 2**: Completed both parts
- **Languages**: Python ✅, Rust ✅, JavaScript ⏳
- **Time to Solve**: 1 hour 52 minutes
- **Difficulty**: ⭐⭐⭐☆☆

### Day 5 (Dec 5, 2025)
- **Challenge**: Cafeteria
- **Part 1**: As the forklifts break through the wall, the Elves are delighted to discover that there was a caf...
- **Part 2**: Completed both parts
- **Languages**: Python ✅, Rust ✅, JavaScript ✅
- **Time to Solve**: 1 hour 9 minutes
- **Difficulty**: ⭐⭐⭐☆☆

### Day 6 (Dec 6, 2025)
- **Challenge**: Trash Compactor
- **Part 1**: After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie...
- **Part 2**: Completed both parts
- **Languages**: Python ✅, Rust ✅, JavaScript ✅
- **Time to Solve**: [Your time here]
- **Difficulty**: ⭐⭐⭐☆☆

### Day 7 (Dec 7, 2025)
- **Challenge**: Laboratories
- **Part 1**: You thank the cephalopods for the help and exit the trash compactor, finding yourself in the fami...
- **Part 2**: Completed both parts
- **Languages**: Python ✅, Rust ✅, JavaScript ✅
- **Time to Solve**: [Your time here]
- **Difficulty**: ⭐⭐☆☆☆

### Day 8 (Dec 8, 2025)
- **Challenge**: Playground
- **Part 1**: Equipped with a new understanding of teleporter maintenance, you confidently step onto the repair...
- **Part 2**: Completed both parts
- **Languages**: Python ✅, Rust ✅, JavaScript ✅
- **Time to Solve**: [Your time here]
- **Difficulty**: ⭐⭐⭐☆☆

### Day 9 (Dec 9, 2025)
- **Challenge**: Movie Theater
- **Part 1**: You slide down the firepole in the corner of the playground and land in the North Pole base movie...
- **Part 2**: Completed both parts
- **Languages**: Python ✅, Rust ✅, JavaScript ✅
- **Time to Solve**: [Your time here]
- **Difficulty**: ⭐⭐⭐☆☆

## 🎯 Goals

- [x] Set up automated file generation
- [x] Create templates for Python, Rust, and JavaScript
- [x] Implement cron job automation
- [ ] Complete all 12 days
- [ ] Optimize solutions for performance
- [ ] Document interesting algorithms used
- [ ] Compare Python vs Rust vs JavaScript execution times

## 🔧 Tools & Technologies

- **Languages**: Python 3.11+, Rust 1.91+, Node.js 18+
- **Automation**: Bash scripts, Cron jobs
- **Version Control**: Git with smart .gitignore
- **Development**: VS Code with extensions

## 📚 Resources

- [Advent of Code 2025](https://adventofcode.com/2025)
- [AoC Reddit Community](https://www.reddit.com/r/adventofcode/)
- [Python Documentation](https://docs.python.org/3/)
- [Rust Documentation](https://doc.rust-lang.org/)
- [JavaScript Documentation (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Node.js Documentation](https://nodejs.org/en/docs/)

## 🏆 Statistics

- **Total Stars**: 18/24 ⭐
- **Days Completed**: 9/12
- **Languages Used**: Python, Rust, JavaScript
- **Automation Level**: Full 🤖

---

*Last updated: December 09, 2025*  
