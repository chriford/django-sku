
document.getElementById("question-remove").addEventListener("click", function(){
  swal({
    title: "Are you sure you want to delete this question?",
    text: "Note: this action cannot be undone.",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  })
  .then((willDelete) => {
    if (willDelete) {
      swal("deleted successfully", {
        icon: 'success', timer: 3000
    })
    }
  });
})
