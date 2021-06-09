console.log("Inside Demo")

const State_drop = document.getElementById("state")

const Dist_drop = document.getElementById("district")

const Pan_drop = document.getElementById("panchayath")

const Ward_drop = document.getElementById("ward")

$.ajax({
    type : 'GET',
    url : 'get-state/',
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
    console.log("State Changed")
    console.log(e.target.value)
    const selected_state = e.target.value

    $.ajax({
        type : 'GET',
        url : `district-json/${selected_state}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            $(Dist_drop).empty().append(('<option value="" disabled selected hidden>Select District...</option>'));
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


Dist_drop.addEventListener('change' , e=>{
    console.log("District Changed")
    console.log(e.target.value)
    const selected_state = e.target.value

    $.ajax({
        type : 'GET',
        url : `ward-pan-json/${selected_state}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            district.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.Panchayath_Name
            Pan_drop.appendChild(option)
        })
        },
        error : function(error){
            console.log(error)
        }
    })
})


Pan_drop.addEventListener('change' , e=>{
    console.log("Panchayath Changed")
    console.log(e.target.value)
    const selected_state = e.target.value

    $.ajax({
        type : 'GET',
        url : `ward-ward-json/${selected_state}/`,
        success : function(response){
            console.log(response)
            const district = response.data
            district.map(item=>{
            const option = document.createElement('option')
            option.value = item.id
            option.innerHTML = item.Ward_Name
            Ward_drop.appendChild(option)
        })
        },
        error : function(error){
            console.log(error)
        }
    })
})