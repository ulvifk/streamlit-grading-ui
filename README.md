# General Plagiarism Checker Usage Guidelines

## Reading Student Files

To process student submissions, use the `ClassRoomBuilder` class to build a classroom from the specified directory. Since some files may be nested within multiple levels of zipped files, you can call the `unzip` method multiple times to handle such cases.

```python
ClassroomBuilder("submissions_dir").unzip().build()
```

- **`unzip()`**: An intermediate operation that can be called repeatedly to ensure all zipped files are extracted.
- **`build()`**: Completes the classroom setup after unzipping the files.

## Checking for Plagiarism

To check for plagiarism, use the `PlagiarismChecker` class. The `PlagiarismChecker` analyzes the submissions and returns a set of tuples, where each tuple contains the names of the files and their corresponding plagiarism similarity score.

```python
(PlagiarismChecker(classroom.students, question_name)
 .cast_to_lower()  # Converts all text to lowercase for case-insensitive comparisons.
 .drop_piece_of_text(start_text, end_text)  # Removes text between specified start and end markers.
 .drop_char(text)  # Removes all occurrences of the specified text.
 .check())  # Returns a set of tuples: { (Student1, Student2, similarity_score) }
```

### Optional Customizations

1. **Remove comments**: To remove all comments from a file, set:
   - `start_text = "#"`, and 
   - `end_text = "\n"`.

2. **Remove docstrings**: To remove docstrings, set:
   - `start_text = """`, and 
   - `end_text = """`.