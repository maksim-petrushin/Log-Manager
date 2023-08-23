document.addEventListener('DOMContentLoaded', () =>{
    document.querySelector('#date').onchange = () => {
        val = document.querySelector('#date').value*1;
        if(val===1){
            document.getElementById("flex-container").style.flexDirection = 'column';
        }
        if(val===2){
            document.getElementById("flex-container").style.flexDirection = 'column-reverse';
        }

    };
    

});