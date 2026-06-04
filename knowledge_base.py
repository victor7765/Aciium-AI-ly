class KnowledgeBase:

    def store(self, original, compressed):

        with open("patterns.txt", "a") as file:

            file.write(f"ORIGINAL: {original}\n")
            file.write(f"COMPRESSED: {compressed}\n")
            file.write("--------------------------\n")