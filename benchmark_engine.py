class BenchmarkEngine:

    def compare(self, original, compressed):

        print("\n[BENCHMARK ENGINE]")

        original_length = len(original)
        compressed_length = len(compressed)

        print("Original Length:", original_length)
        print("Compressed Length:", compressed_length)

        if compressed_length < original_length:
            print("Compression successful.")
        else:
            print("No optimization improvement.")