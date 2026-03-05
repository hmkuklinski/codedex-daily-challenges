//implementation using lists:
function findMissingColors(grid) {
  //list of valid colors:
  let colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"];
  //list of colors:
  let found_colors = [];

  //go through each item, if not in found_colors, add color to list:
  for(let i=0;i<grid.length;i++){
    for(let j=0;j<grid[i].length;j++){
      let currentColor = grid[i][j];
      //adding only if color not in found_colors list:
      if (!found_colors.includes(currentColor)){
        found_colors.push(currentColor);
      }
    }
  }

  //go through and see what colors are not added in list:
  let not_found = [];
  for(let i=0;i<colors.length;i++){
    //indexOf returns -1 only if not found--> add to not_found list:
    if (found_colors.indexOf(colors[i]) ==-1 ){
      not_found.push(colors[i]);
    }
  }
  //return not found
  return not_found  
}

// let input1= [["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
//   ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
//   ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
//   ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
//   ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
//   ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
//   ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]];

// console.log(findMissingColors(input1));

// let input2 = [["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟧"],     
// ["🟨", "🟩", "🟦", "🟥", "🟨", "🟩", "🟦"],     
// ["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟨"],     
// ["🟩", "🟦", "🟥", "🟧", "🟨", "🟩", "🟦"],     
// ["🟨", "🟥", "🟧", "🟨", "🟩", "🟦", "🟥"],     
// ["🟦", "🟩", "🟨", "🟥", "🟧", "🟩", "🟦"],    
// ["🟥", "🟧", "🟨", "🟩", "🟦", "🟨", "🟥"]];

// console.log(findMissingColors(input2));



