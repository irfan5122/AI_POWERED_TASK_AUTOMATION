import re
text = "create a file hello.txt"
pattern = r'\b\w+\.\w+\b'
matches = re.findall(pattern, text)

'''sentences = [
    "create a file hello.txt",
    "delete the file test_document.pdf",
    "download image.png and video.mp4",
    "open the report.docx and review",
    "save it as data.csv",
    "random text without a file name"
]

for sentence in sentences:
    print(f"Input: {sentence}")
    print(f"Extracted File Names: {extract_filenames(sentence)}\n")
'''
print(matches)