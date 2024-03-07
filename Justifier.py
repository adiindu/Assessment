import argparse
import sys

class ParagraphJustifier():
    def __init__(self, paragraph, page_width):
        self.paragraph = paragraph
        self.page_width = page_width

    def justify_paragraph(self):
        words = self.paragraph.split()
        lines = []
        current_line = []
        current_line_width = 0

        for word in words:
            if current_line_width + len(word) + len(current_line) > self.page_width:
                lines.append(current_line)
                current_line = [word]
                current_line_width = len(word)
            else:
                current_line.append(word)
                current_line_width += len(word)

        if current_line:
            lines.append(current_line)

        justified_lines = []
        for line in lines:
            spaces_to_add = self.page_width - sum(len(word) for word in line)
            num_gaps = len(line) - 1

            if num_gaps > 0:
                spaces_per_gap = spaces_to_add // num_gaps
                extra_spaces = spaces_to_add % num_gaps

                justified_line = line[0]
                for i, word in enumerate(line[1:]):
                    justified_line += ' ' * (spaces_per_gap + (1 if i < extra_spaces else 0)) + word

                justified_lines.append(justified_line)
            else:
                justified_lines.append(line[0].ljust(self.page_width))

        return justified_lines

def main():
    parser = argparse.ArgumentParser(description="Justify a paragraph with a specified page width.")
    parser.add_argument("paragraph", help="Input paragraph to be justified.")
    parser.add_argument("page_width", type=int, help="Width of the page for justification.")

    args = parser.parse_args()
    
    try:
        justifier = ParagraphJustifier(args.paragraph, args.page_width)
        justified_paragraph = justifier.justify_paragraph()

        for i, line in enumerate(justified_paragraph, start=1):
            print(f"Array [{i}] = \"{line}\"")
    except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        
if __name__ == '__main__':
    main()
