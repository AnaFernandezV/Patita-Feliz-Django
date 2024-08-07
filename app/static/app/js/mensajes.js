
/*/ ejemplo /*/

function confirmDelete(codigo) {
  Swal.fire({
      icon: 'warning',
      title: 'Estás seguro?',
      text: 'No podrás deshacer la acción!',
      showCancelButton: true,
      cancelButtonColor: "#d33",
      confirmButtonText: "Si, Eliminar!",
      confirmButtonColor: '#0292c9',
      cancelButtonText: "Cancelar"
    }).then((result) => {
      if (result.value) {
        Swal.fire(
          'Eliminado!',
          'Producto eliminado Correctamente',
          'success'
        ).then(function() {
          window.location.href = "/eliminar/"+ codigo +"/"
        })
      }
    })
}


function eliminarUsu(run) {
  Swal.fire({
      icon: 'warning',
      title: 'Estás seguro?',
      text: 'No podrás deshacer la acción!',
      showCancelButton: true,
      cancelButtonColor: "#d33",
      confirmButtonText: "Si, Eliminar!",
      confirmButtonColor: '#3085d6',
      cancelButtonText: "Cancelar"
    }).then((result) => {
      if (result.value) {
        Swal.fire(
          'Eliminado!',
          'Usuario eliminado Correctamente',
          'success'
        ).then(function() {
          window.location.href = "/eliminar_usuario/"+ run +"/"
        })
      }
    })
}


/*/ function exitoCambios(codigo) {
  Swal.fire({
    icon: 'success',
    title: 'Cambios guardados exitosamente!',
    showConfirmButton: true
  }).then(function() {
        window.location.href = "/listar_producto/"
      })
}

function exitoAdd() {
  Swal.fire({
    icon: 'success',
    title: 'Producto agregado exitosamente!',
    showConfirmButton: true,
  }).then(function() {
        window.location.href = "/listar_producto/"
      })
}

/*/