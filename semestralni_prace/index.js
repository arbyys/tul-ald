var app = new Vue({
    el: '#app',
    data: {
        grid: [...Array(20)].map(_ => Array(20).fill(-1)),
        properties: ["1111", "0101", "1010", "0011", "0110", "1100", "1001", "0111", "1011", "1110", "1101", "0010", "0001", "0100", "1000"],
        allowed: [true, true, true, true, true, true, true, true, true, true, true, true, true, true, true],
        adjacent: [],
        currentAllowed: []
    },
    mounted: function () {

    },
    methods: {

        getRandomNumber: function (max) {
            return Math.random() * max | 0;
        },

        getRandomAdjacent: function () {
            if (this.gridIsEmpty()) {
                return [this.getRandomNumber(this.gridDimension), this.getRandomNumber(this.gridDimension)]
            }

            randomIndex = this.getRandomNumber(this.adjacent.length);
            selected = this.adjacent[randomIndex];
            this.adjacent.splice(randomIndex, 1);
            return selected;
        },

        addAllAdjacent: function (randomPos) {
            for (let i = 0; i < 4; i++) {
                currentPos = [...randomPos];
                switch (i) {
                    case 0: // up
                        if (currentPos[0] == 0) {
                            continue;
                        }
                        currentPos[0] -= 1;
                        break;
                    case 1: // right
                        if (currentPos[1] == this.gridDimension - 1) {
                            continue;
                        }
                        currentPos[1] += 1;
                        break;
                    case 2: // down
                        if (currentPos[0] == this.gridDimension - 1) {
                            continue;
                        }
                        currentPos[0] += 1;
                        break;
                    case 3: // left
                        if (currentPos[1] == 0) {
                            continue;
                        }
                        currentPos[1] -= 1;
                        break;
                }
                if (!(this.adjacent.some(row => JSON.stringify(row) === JSON.stringify(currentPos))) && this.grid[currentPos[0]][currentPos[1]] == -1) {
                    this.adjacent.push([currentPos[0], currentPos[1]])
                }
            }
        },

        getAllAllowed: function () {
            let returnValues = []
            for (let index = 0; index < this.allowed.length; ++index) {
                if (this.allowed[index]) {
                    returnValues.push(index)
                }
            }
            return returnValues
        },

        setCharAt: function (str, index, chr) {
            if (index > str.length - 1) return str;
            return str.substring(0, index) + chr + str.substring(index + 1);
        },

        getRandomMatchingTile: function (pos) {
            let mask = "xxxx"
            for (let i = 0; i < 4; i++) {
                currentPos = [...pos];
                switch (i) {
                    case 0: // up
                        if (currentPos[0] == 0) {
                            continue;
                        }
                        currentPos[0] -= 1;
                        selectedItem = this.grid[currentPos[0]][currentPos[1]]
                        if (selectedItem != -1 && selectedItem != -2) {
                            mask = this.setCharAt(mask, 0, this.properties[selectedItem - 1].toString().charAt(2))
                        }
                        break;
                    case 1: // right
                        if (currentPos[1] == this.gridDimension - 1) {
                            continue;
                        }
                        currentPos[1] += 1;
                        selectedItem = this.grid[currentPos[0]][currentPos[1]]
                        if (selectedItem != -1 && selectedItem != -2) {
                            mask = this.setCharAt(mask, 1, this.properties[selectedItem - 1].toString().charAt(3))
                        }
                        break;
                    case 2: // down
                        if (currentPos[0] == this.gridDimension - 1) {
                            continue;
                        }
                        currentPos[0] += 1;
                        selectedItem = this.grid[currentPos[0]][currentPos[1]]
                        if (selectedItem != -1 && selectedItem != -2) {
                            mask = this.setCharAt(mask, 2, this.properties[selectedItem - 1].toString().charAt(0))
                        }
                        break;
                    case 3: // left
                        if (currentPos[1] == 0) {
                            continue;
                        }
                        currentPos[1] -= 1;
                        selectedItem = this.grid[currentPos[0]][currentPos[1]]
                        if (selectedItem != -1 && selectedItem != -2) {
                            mask = this.setCharAt(mask, 3, this.properties[selectedItem - 1].toString().charAt(1))
                        }
                        break;
                }

            }
            filtered = [];
            for (const index of this.currentAllowed) {
                element = this.properties[index]
                allDifferent = true
                for (var i = 0; i < element.length; i++) {
                    current = element.charAt(i)
                    if (mask.toString().charAt(i) === "x") {
                        continue
                    }
                    if (mask.toString().charAt(i) != current) {
                        allDifferent = false
                    }
                }
                if (allDifferent) {
                    filtered.push(element)
                }
            }
            if (filtered.length == 0) {
                return -2
            }
            return this.properties.indexOf(filtered[this.getRandomNumber(filtered.length)]) + 1
        },

        generate: async function () {
            this.grid = [...Array(20)].map(_ => Array(20).fill(-1))
            this.currentAllowed = this.getAllAllowed()
            while (!this.gridIsFull()) {
                randomPos = this.getRandomAdjacent()
                randomItem = this.getRandomMatchingTile(randomPos)
                Vue.set(this.grid[randomPos[0]], randomPos[1], randomItem);
                this.addAllAdjacent(randomPos)
                await new Promise(resolve => setTimeout(resolve, 1));

            }
        },

        gridIsEmpty: function () {
            for (let i = 0; i < this.grid.length; ++i) {
                const arr = this.grid[i];
                for (let j = 0; j < arr.length; ++j) {
                    if (this.grid[i][j] != -1) {
                        return false;
                    }
                }
            }
            return true;
        },
        gridIsFull: function () {
            for (let i = 0; i < this.grid.length; ++i) {
                const arr = this.grid[i];
                for (let j = 0; j < arr.length; ++j) {
                    if (this.grid[i][j] == -1) {
                        return false;
                    }
                }
            }
            return true;
        },

    },
    computed: {
        gridDimension() {
            return this.grid.length;
        }
    }
})