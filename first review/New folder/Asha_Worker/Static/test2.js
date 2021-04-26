console.log("--------------------test2-----------------------------")

const staff_pan = document.getElementById("staff_panch")

const staff_ward = document.getElementById("staff_ward")

$.ajax({
    type : 'GET',
    url : 'Add_Asha/get-pan-json/',
    success : function(response){
        console.log(response.data)
        const state = response.data
        $(staff_pan).empty().append(('<option value="" disabled selected hidden>Choose Panchayath/Muncipality</option>'));
        state.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.Panchayath_Name
            staff_pan.appendChild(option)
        })
    },
    error : function(error){
        console.log(error)
    }
})



staff_pan.addEventListener('change' , e =>{
    console.log("Hai changed data")
    console.log(e.target.value)
    const selected_dist = e.target.value

    $.ajax({
        type : 'GET',
        url : `ward-json/${selected_dist}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            $(staff_ward).empty().append(('<option value="" disabled selected hidden>Choose Ward</option>'));
            //$.each(response.data, function (i, p) {
               // $(org_dist).append($('<option></option>').val(p.SkillID).html(p.SkillName));
              //});
         
            district.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.Ward_Name
            staff_ward.appendChild(option)
        })
        },
        error : function(error){
            console.log(error)
        }
    })
})
