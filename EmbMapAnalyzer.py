import re
import argparse
from collections import defaultdict

def parse_map_file(map_file_path):
    # Define regex pattern to categorize main sections
    section_pattern = re.compile(
        r'^\s*(?P<main_section>\.(?:text|data|bss))(?:\.\w+)*\s*'
        r'(?P<start>0x[0-9a-fA-F]+)\s+'
        r'(?P<size>0x[0-9a-fA-F]+)\s+'
        r'(?P<file>[\w/\\\-.]+\.o)'
    )

    # Statistics by module and section
    module_stats = defaultdict(lambda: defaultdict(int))
    total_sizes = defaultdict(int)

    with open(map_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = section_pattern.search(line)
            if match:
                main_section = match.group('main_section')
                size_str = match.group('size')
                try:
                    size = int(size_str, 16)
                except ValueError:
                    print(f"Failed to convert size {size_str}, line: {line.strip()}")
                    continue
                file_name = match.group('file')

                # Accumulate sizes
                module_stats[file_name][main_section] += size
                total_sizes[main_section] += size
            else:
                # print(f"Unmatched line: {line.strip()}")
                pass

    return module_stats, total_sizes

def print_report(module_stats, total_sizes):
    # Print total memory usage
    print("=== Total Memory Usage ===")
    for section, size in total_sizes.items():
        print(f"{section}: {size} bytes")

    # Print module-wise statistics
    print("\n=== Module Statistics ===")
    for module, sections in sorted(module_stats.items(), key=lambda x: sum(x[1].values()), reverse=True):
        total = sum(sections.values())
        print(f"\nModule: {module}")
        for section, size in sections.items():
            print(f"  {section}: {size} bytes")
        print(f"  Total: {total} bytes")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='ELF Map File Analyzer')
    parser.add_argument('--map', required=True, help='Path to .map file')
    args = parser.parse_args()
    
    module_stats, total_sizes = parse_map_file(args.map)
    print_report(module_stats, total_sizes)
