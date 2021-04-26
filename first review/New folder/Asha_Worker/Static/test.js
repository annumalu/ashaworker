console.log("Inside test") 

const drop_data = document.getElementById("ward_district")

const pan = document.getElementById("ward_pan")

drop_data.addEventListener('change' , e =>{
    console.log("Hai ")
    console.log(e.target.value)
    const selected_dist = e.target.value

    $.ajax({
        type : 'GET',
        url : `ward-pan-json/${selected_dist}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            $(pan).empty().append(('<option value="" disabled selected hidden>Choose Panchayath/Muncipality</option>'));
            district.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.Panchayath_Name
            pan.appendChild(option)
        })
        },
        error : function(error){
            console.log(error)
        }
    })
})





