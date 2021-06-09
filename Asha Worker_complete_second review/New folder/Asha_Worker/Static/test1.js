console.log("huubuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")


const org = document.getElementById("org_state")

const org_dist = document.getElementById("org_dist")


org.addEventListener('change' , e =>{
    console.log("Hai changed data")
    console.log(e.target.value)
    const selected_dist = e.target.value

    $.ajax({
        type : 'GET',
        url : `district-json/${selected_dist}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            $(org_dist).empty().append(('<option value="" disabled selected hidden>Choose District</option>'));
            //$.each(response.data, function (i, p) {
               // $(org_dist).append($('<option></option>').val(p.SkillID).html(p.SkillName));
              //});
         
            district.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.District_Name
            org_dist.appendChild(option)
        })
        },
        error : function(error){
            console.log(error)
        }
    })
})



