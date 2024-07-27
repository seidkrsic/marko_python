from datetime import datetime

class Printer:
    def __init__(self, brand, model):
        self._print_queue = []
        self._brand = brand
        self._model = model

    def add_document(self, filename, document):
        """Add a document to the print queue."""
        self._print_queue.append((filename, document))

    def print_document(self):
        """Print the first document in the print queue."""
        if self._print_queue:
            document = self._print_queue.pop(0)
            print(f"Printing document: {document[0]}")
            return document[1]
        else:
            print("No documents in the print queue.")
            return None

    def search_document(self, filename):
        """Search for a document in the print queue by filename."""
        for doc in self._print_queue:
            if doc[0] == filename:
                return doc[1]
        print(f"Document {filename} not found in the print queue.")
        return None

    def __del__(self):
        self._print_queue = None

class ScannerOCR:
    def __init__(self, resX, resY):
        self._resX = resX
        self._resY = resY

    def scan_ocr(self):
        """Simulate scanning a document and performing OCR."""
        sid = open_scanner()
        if sid.onoff():
            text = sid.read_text()
            sid.close_scanner()
            return text
        else:
            print("Scanner is off.")
            return None

    def __del__(self):
        pass

class MultifunctionalDevice(ScannerOCR, Printer):
    def __init__(self, brand, model, resX, resY):
        Printer.__init__(self, brand, model)
        ScannerOCR.__init__(self, resX, resY)

    def photocopy(self):
        """Scan a document and add it to the print queue."""
        text = self.scan_ocr()
        if text:
            filename = "copy_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
            self.add_document(filename, text)
            print(f"Document {filename} added to print queue.")
        else:
            print("Failed to scan document.")

    def __del__(self):
        Printer.__del__(self)

# Dummy implementations for the open_scanner function and related methods
class DummyScanner:
    def onoff(self):
        return True
    
    def read_text(self):
        return "Scanned text content"
    
    def close_scanner(self):
        pass

def open_scanner():
    return DummyScanner()

# Example usage
if __name__ == "__main__":
    # Printer example
    printer = Printer("HP", "LaserJet 1020")
    printer.add_document("doc1.txt", "This is the first document.")
    printer.add_document("doc2.txt", "This is the second document.")
    print(printer.print_document())  # Output: This is the first document.
    print(printer.search_document("doc2.txt"))  # Output: This is the second document.

    # Scanner example
    scanner = ScannerOCR(300, 300)
    print(scanner.scan_ocr())  # Output: Scanned text content

    # MultifunctionalDevice example
    multi_device = MultifunctionalDevice("Canon", "MX490", 300, 300)
    multi_device.photocopy()
    print(multi_device.print_document())  # Output: Scanned text content
multi_device.__del__() 