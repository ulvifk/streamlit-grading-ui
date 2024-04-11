import difflib
import subprocess

# The inputs you want to send to the original script
inputs = ("1\n" +
          "-5\n" +
          "-5\n" +
          "-7\n" +
          "5\n" +
          "2\n" +
          "11 \n" +
          "32 \n" +
          "2 \n" +
          "7 \n")


def do_for(file: str):
    # Note: Each input is followed by a newline character ('\n') to simulate the Enter key press

    # Running the original script as a subprocess and passing the inputs
    process = subprocess.Popen(['python', file], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)

    # Sending inputs to the original script
    output, errors = process.communicate(input=inputs)

    return output

def find_differing_characters(str1, str2):
    differing_chars = []
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            differing_chars.append((str1[i], str2[i]))
    if len(str1) != len(str2):
        longer_str = str1 if len(str1) > len(str2) else str2
        extra_chars = longer_str[min(len(str1), len(str2)):]
        differing_chars.extend([(char, '') for char in extra_chars] if longer_str is str1 else [('', char) for char in extra_chars])
    print(differing_chars)

#test_output = (do_for("test.py").replace(" ", "")
        #       .replace("\n", "").replace(".", "")
          #     .replace(",", "").replace(":", "")
           #    .lower())
#dummy_output = (do_for("dummy.py").replace(" ", "").replace("\n", "")
        #        .replace(".", "").replace(",", "")
          #      .replace(":", "")
          #      .lower())

dummy_output = ''.join(c for c in do_for('dummy.py') if c.isdigit())
test_output = ''.join(c for c in do_for('test.py') if c.isdigit())


if test_output != dummy_output:
    find_differing_characters(test_output, dummy_output)

print(do_for("test.py"))
print()
print(do_for("dummy.py"))
