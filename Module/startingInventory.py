from Class.locationClass import KH2StartingItem

class StartingInventory:
    def generateStartingInventory(inventory, itemsToAdd):
        for item in itemsToAdd:
            inventory.setReward(int(item))


    def getOptions():
        return {
            "moduleName": "Sora's Starting Inventory",
            "options":{
                "Abilities": [
                    {138: "Scan"},
                ],
                "Items": [
                    {537: "Hades Cup Trophy"},
                    {369: "Membership Card"}
                ]
            }
        }

    def getIdConverter():
        return {
            '138':"Scan",
            '537':"Hades Cup Trophy",
            '369':"Membership Card"
        }