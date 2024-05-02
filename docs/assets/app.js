import EasterCalculus from "./easterLib.js"

function logics(){
    const tableBodyElement = document.querySelector("main table tbody")
    const yearHolder = document.getElementById("year-holder")
    const templateRow = tableBodyElement.querySelector("tr")
    const modes = ["JulianInGregorian","GaussJulianInGregorian","GaussGregorian","AnonymousGregorian","AnonymousGregorianOptimized","Julian","GaussJulian"]
    let currentYear = new Date().getFullYear()
    templateRow.remove()
    let lang = "bg"

    function setYear(){
        const prev = document.createElement("span")
        prev.textContent = "⮜"
        prev.className = "year-decrease"
        const next = document.createElement("span")
        next.textContent = "⮞"
        next.className = "year-increase"
        const year = document.createElement("span")
        year.textContent = currentYear
        yearHolder.innerHTML = ""
        yearHolder.append(prev,year,next)
        prev.addEventListener("click",e=>{ currentYear--; year.textContent = currentYear; load(currentYear);})
        next.addEventListener("click",e=>{ currentYear++; year.textContent = currentYear; load(currentYear);})
    }

    const translations = {
        bg:{
            year: "година",
            day: "ден",
            month:"месец",
            calendar:"календар",
            leap:"високосна",
            JulianInGregorian:"юлиански в григориански",
            GaussJulianInGregorian:"юлиански в григориански - гаус",
            GaussGregorian:" григориански - гаус",
            AnonymousGregorian:"анонимен григориански",
            AnonymousGregorianOptimized:" анонимен григориански - оптимизиран",
            Julian:"юлиански",
            GaussJulian:"юлиански - гаус",
            months:[null,"януари","февруари","март","април","май","юни","юли","август","септември","октомври","ноември","декември"],
            bools:{true:"✔",false:"X"}

        }
    }

    function addRow(year,month,day,calendar,leap){
        const newRow = templateRow.cloneNode(true)
        const fields = newRow.querySelectorAll("td");
        [calendar,year,month,day,leap].forEach((el,idx)=>fields[idx].textContent = el)
        tableBodyElement.append(newRow)
    }

    function addData(year,mode){
        const {month,day,leap} = new EasterCalculus(year,mode)
        // addRow(year,month,day,mode.match(/[A-Z]?[a-z]*/gm).filter(el=>el).join(" "),leap)
        addRow(year,translations[lang].months[month],day,translations[lang][mode],translations[lang].bools[leap])
    }

    function load(year){
        tableBodyElement.innerHTML = ""
        modes.forEach(mode=>addData(Number(year),mode))
    }

    setYear()
    load(currentYear)
}

logics()