def get_words_from_file(file):
  file_contents = file.read()
  book = file_contents.lower()
  words = book.split()
  return words

def get_letter_count_dictionary(words):
  dict = {}

  for word in words:
      lowered = word.lower()

      for letter in lowered:
        if letter.isalpha():
          if letter not in dict:
            dict[letter] = 1
          else:
            dict[letter] += 1
  return dict

def sort_on(dict):
  return dict["count"]

def main():
  with open("./books/frankenstein.txt") as f:
    words = get_words_from_file(f)
    letter_count_dict = get_letter_count_dictionary(words)

    print(letter_count_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    letter_count_list = []

    for letter in letter_count_dict:
      letter_count_list.append({ "character": letter, "count": letter_count_dict[letter] })

  letter_count_list.sort(reverse=True, key=sort_on)

  for record in letter_count_list:
    print(f"The '{record["character"]}' character was found {record["count"]} times")

main()