#preprocessing


def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Split the text into lines
    lines = text.split('\n')
    # Initialize the main heading variable
    main_heading = None

    processed_lines = []
    for line in lines:
        line = line.strip()
        # Detect if the line might be a new main heading (no dash starting and no continuation of a list)
        if not re.match(r'^[\–\-\•]', line) and len(line.split()) > 1:
            main_heading = line  # Update main heading
            processed_lines.append(line)  # Append the line itself as a main heading
        elif line.startswith('–'):
            # Remove leading dash and prepend the current main heading
            line = re.sub(r'^\–\s*', '', line)
            if main_heading:
                processed_lines.append(main_heading + ' ' + line)
            else:
                processed_lines.append(line)  # Just in case no main heading has been set yet
        else:
            processed_lines.append(line)  # Just append the line as is if it doesn't start with a dash

    # Join the processed lines back into a single string
    return '\n'.join(processed_lines)

# Example usage
ABC = """
Fuzzy String Matching
– String comparison process – similarity between strings, such as in a spell checker.
– Algorithms reduce to linear algebra concepts such as similarity between vectors (dot product and cosine similarity).
– Three measures bla bla
some new subheading
Package “textclean”
– Tools to clean and process text
– Can easily handle emoticons in text which is not an easy task for the other text mining packages
– replace_emoticon() function replaces emoticons with word equivalents
Package “readtext”
– to read in different types of text data
"""
print(preprocess_text(ABC))
