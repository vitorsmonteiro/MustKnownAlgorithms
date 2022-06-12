const compareTwoNumbers = (a, b) => {
    console.assert(typeof a === "number");
    console.assert(typeof b === "number");
    if (Math.round(a * 100) / 100 > Math.round(b * 100) / 100) {
        return "a > b";
    } else if (Math.round(a * 100) / 100 < Math.round(b * 100) / 100) {
        return "a < b";
    } else {
        return "a = b";
    }
}

console.log(compareTwoNumbers("3", 3))
