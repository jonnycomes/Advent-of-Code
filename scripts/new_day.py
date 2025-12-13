#!/usr/bin/env python3
"""
Script to create a new day folder structure for Advent of Code
Usage: python new_day.py <year> <day>
"""

import sys
import shutil
from pathlib import Path

def create_day_folder(year, day):
    """Create folder structure for a new day"""
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Create year/dayXX folder
    day_folder = project_root / str(year) / f"day{day:02d}"
    day_folder.mkdir(parents=True, exist_ok=True)
    
    # Create empty input file
    input_path = day_folder / "input.txt"
    input_path.touch()
    print(f"✅ Created {input_path}")
    
    # Create empty instructions file
    instructions_path = day_folder / "instructions.md"
    instructions_path.touch()
    print(f"✅ Created {instructions_path}")

    # Copy template solution
    template_path = project_root / "utils" / "templates" / "solution.py"
    solution_path = day_folder / "solution.py"
    
    if template_path.exists():
        shutil.copy2(template_path, solution_path)
        print(f"✅ Created {solution_path}")
    else:
        print(f"⚠️  Template not found at {template_path}")
    
    print(f"\n🎄 Day {day} setup complete!")
    print(f"📁 Folder: {day_folder}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python new_day.py <year> <day>")
        print("Example: python new_day.py 2025 1")
        sys.exit(1)
    
    try:
        year = int(sys.argv[1])
        day = int(sys.argv[2])
        
        if day < 1 or day > 25:
            print("Day must be between 1 and 25")
            sys.exit(1)
            
        create_day_folder(year, day)
        
    except ValueError:
        print("Year and day must be integers")
        sys.exit(1)

if __name__ == "__main__":
    main()
