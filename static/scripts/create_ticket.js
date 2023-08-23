document.addEventListener('DOMContentLoaded', () =>{
    document.querySelector('select').onchange = () => {
        val = document.querySelector('select').value*1
        if(val<7){
            document.getElementById("description").style.display = 'block';
        }
        else{
            let myForm = document.getElementById("create_ticket");
            myForm.querySelectorAll(":scope > div").forEach(div =>{
                div.style.display = 'none';
            });
        }

    }
});