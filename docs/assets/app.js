import EasterCalculus from "./easterLib.js"

function logics(){
    const tableBodyElement = document.querySelector("main table tbody")
    const yearHolder = document.getElementById("year-holder")
    const templateRow = tableBodyElement.querySelector("tr")
    const modes = ["JulianInGregorian","GaussJulianInGregorian","GaussGregorian","AnonymousGregorian","AnonymousGregorianOptimized","Julian","GaussJulian"]
    templateRow.remove()

    function addRow(year,month,day,calendar,leap){
        const newRow = templateRow.cloneNode(true)
        const fields = newRow.querySelectorAll("td");
        [calendar,year,month,day,leap].forEach((el,idx)=>fields[idx].textContent = el)
        tableBodyElement.append(newRow)
    }

    function addData(year,mode){
        const {month,day,leap} = new EasterCalculus(year,mode)
        addRow(year,month,day,mode.match(/[A-Z]?[a-z]*/gm).filter(el=>el).join(" "),leap)
    }

    modes.forEach(mode=>addData(Number(yearHolder.textContent),mode))
}

logics()