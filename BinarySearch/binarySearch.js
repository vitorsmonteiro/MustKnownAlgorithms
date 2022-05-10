const generate_array = (n_items) => {
    let ordered_list = []
    for (let i=0; i<n_items; i++) {
        ordered_list.push(parseInt(100*Math.random()))
    }
    return ordered_list.sort((a, b) => {return(a - b)})
}

const binary_search = (ordered_list, target, start_idx=false, end_idx=false) => {
    start_idx = start_idx ? start_idx : 0
    end_idx = end_idx===false ? ordered_list.length-1 : end_idx

    let middle_idx = parseInt((end_idx + start_idx) / 2)

    if (start_idx === end_idx){
        return false
    }
    if (target === ordered_list[middle_idx]){
        return middle_idx
    }   
    else if (target < ordered_list[middle_idx]){
        return binary_search(ordered_list, target, start_idx, middle_idx)
    } else{
        return binary_search(ordered_list, target, middle_idx+1, end_idx)
    }
}

const list_size = 10
const ordered_list = generate_array(list_size)
const target = parseInt(100*Math.random())
console.log(ordered_list)
console.log(`Target = ${target}`)
const idx = binary_search(ordered_list, target)
console.log(idx ? idx : "Target not found")