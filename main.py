"""
This Add-On allows you to bulk delete tags and/or key value pairs from a set of documents. 
"""

from documentcloud.addon import AddOn

class BulkDeleteTags(AddOn):
    """DocumentCloud Add-On to bulk remove tags"""

    def main(self):
        """The main add-on functionality goes here."""
        # fetch your add-on specific data
        del_key = self.data.get("del_key")
        for document in self.get_documents():
            if del_key in document.data:
                document.data.pop(del_key)
                print(document.data)
                document.save()

if __name__ == "__main__":
    BulkDeleteTags().main()
