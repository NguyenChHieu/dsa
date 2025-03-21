class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for ingre in ingredients[i]:
                graph[recipes[i]].append(ingre)

        r = set(recipes)
        s = set(supplies)
        visited = set()

        def cook(recipe):
            if recipe in s:  # an ingredient/ a recipe which alr computed
                return True
            if recipe in visited:
                return False
            visited.add(recipe)
            for nb in graph[recipe]:
                if nb in s:  # ingredient exist
                    continue
                if nb in r:  # if its a recipe not computed yet
                    if cook(nb):
                        continue
                    return False
                return False  # ingredient not exist
            s.add(recipe)
            return True

        ans = []
        for re in recipes:
            if cook(re):
                ans.append(re)
        return ans
