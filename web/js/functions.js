

function ToggleList(IDS) {
  var CState = document.getElementById(IDS);
  if (CState.style.display != "block") { CState.style.display = "block"; }
                                  else { CState.style.display = "none"; }
}

