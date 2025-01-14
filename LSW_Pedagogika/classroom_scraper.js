const listOfAllMaterials = [];
let materialsAsText = '';
const days = document.querySelectorAll('.n4xnA');
days.forEach(day => {
  const date  = day.querySelector('.dDKhVc').innerText;
  const allDateMaterials = day.querySelectorAll('.vwNuXe');
  allDateMaterials.forEach(material => {
    const materialLink = material.href;
    const materialTitle = material.querySelector('.A6dC2c').innerText;
    materialsAsText += `${date}, ${materialLink}, ${materialTitle}\n`;
  })
})
console.log(materialsAsText)


  // const dateTitle = day.querySelector('.pco8Kc').innerText;
 //  ${dateTitle},


    // listOfAllMaterials.push({
    //   date,
    //   dateTitle,
    //   title: materialTitle,
    //   link: materialLink
    // })