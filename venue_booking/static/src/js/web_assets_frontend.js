function venueOnchange(){
    var name = document.getElementById("name").value;
    var phone = document.getElementById("phone").value;
    var mail = document.getElementById("mail").value;
    var specity = document.getElementById("specity").value;
    var organization = document.getElementById("organization").value;
    var venue = document.getElementById("venue_id").value;
    var url = "//" + window.location.hostname + ":8069" + window.location.pathname + "?types=" + venue;

    sessionStorage.setItem("name", name);
    sessionStorage.setItem("phone", phone);
    sessionStorage.setItem("mail", mail);
    sessionStorage.setItem("specity", specity);
    sessionStorage.setItem("organization", organization);
    sessionStorage.setItem("venue", venue);
    location.replace(url);
}

console.log("####################################");

if (sessionStorage.getItem("venue") != null) {
    document.getElementById("name").value = sessionStorage.getItem("name");
    document.getElementById("phone").value = sessionStorage.getItem("phone");
    document.getElementById("mail").value = sessionStorage.getItem("mail");
    document.getElementById("specity").value = sessionStorage.getItem("specity");
    document.getElementById("organization").value = sessionStorage.getItem("organization");
    document.getElementById("venue_id").value = sessionStorage.getItem("venue");
    sessionStorage.clear();
}

function facilityOnchange(n){
    console.log(n.value);
    if (document.getElementById("abc").value == ""){
        document.getElementById("abc").value = document.getElementById("abc").value + n.value;
    }else{
        document.getElementById("abc").value = document.getElementById("abc").value + "," + n.value;
    }
    var html = `<div class="form-control d-flex flex-row justify-content-between facility" onclick="facilityRemove(this)">
                    <span>${n.options[n.selectedIndex].text}</span>
                </div>`;
    n.options[n.selectedIndex].remove();
    document.getElementById("facility_id").insertAdjacentHTML("beforebegin", html);
}

function facilityRemove(n){
    n.remove();
}

