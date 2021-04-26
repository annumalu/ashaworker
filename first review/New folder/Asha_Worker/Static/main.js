console.log("Heloo Working Me")

const State_drop = document.getElementById("state_id")

const Dist_drop = document.getElementById("district")

const Ward_State_drop = document.getElementById("ward_kerala")

const Ward_Dist_drop = document.getElementById("ward_district")


$.ajax({
    type : 'GET',
    url : 'state-json/',
    success : function(response){
        console.log(response.data)
        const state = response.data
        state.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.State_Name
            State_drop.appendChild(option)
        })
    },
    error : function(error){
        console.log(error)
    }
})

State_drop.addEventListener('change' , e=>{
    console.log("Changed")
    console.log(e.target.value)
    const selected_state = e.target.value

    $.ajax({
        type : 'GET',
        url : `district-json/${selected_state}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            $(Dist_drop).empty().append(('<option value="" disabled selected hidden>Choose District</option>'));
            district.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.District_Name
            Dist_drop.appendChild(option)
        })
        },
        error : function(error){
            console.log(error)
        }
    })
})


$.ajax({
    type : 'GET',
    url : 'ward-state-json/',
    success : function(response){
        console.log(response.data)
        const state = response.data
        state.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.State_Name
            Ward_State_drop.appendChild(option)
        })
    },
    error : function(error){
        console.log(error)
    }
})


Ward_State_drop.addEventListener('change' , e=>{
    console.log("Changed")
    console.log(e.target.value)
    const selected_state = e.target.value

    $.ajax({
        type : 'GET',
        url : `ward-district-json/${selected_state}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            $(Ward_Dist_drop).empty().append(('<option value="" disabled selected hidden>Choose District</option>'));
            district.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.District_Name
            Ward_Dist_drop.appendChild(option)
        })
        },
        error : function(error){
            console.log(error)
        }
    })

})




