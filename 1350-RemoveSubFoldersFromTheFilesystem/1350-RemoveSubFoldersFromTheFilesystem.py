# Last updated: 08/02/2026, 14:28:06
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        
        # Initialize the result list with no subfolders
        result = []
        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result