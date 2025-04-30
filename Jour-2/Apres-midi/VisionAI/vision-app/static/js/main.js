document.addEventListener('DOMContentLoaded', function () {
    // Référence au formulaire
    const form = document.querySelector('form');
    const fileInput = document.getElementById('file');

    if (form) {
        // Ajouter une classe lors de la soumission pour indiquer le chargement
        form.addEventListener('submit', function (e) {
            // Vérifier si un fichier a été sélectionné
            if (fileInput && fileInput.files.length > 0) {
                // Vérifier la taille du fichier (max 5MB)
                if (fileInput.files[0].size > 5 * 1024 * 1024) {
                    e.preventDefault();
                    alert('Le fichier est trop volumineux. Veuillez choisir un fichier de moins de 5MB.');
                    return;
                }

                // Ajouter la classe de chargement
                document.querySelector('.card-body').classList.add('loading');
            }
        });

        // Prévisualisation de l'image (optionnel)
        if (fileInput) {
            fileInput.addEventListener('change', function () {
                // Code pour prévisualisation si nécessaire
            });
        }
    }

    // Initialiser les tooltips Bootstrap (si utilisés)
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    if (typeof bootstrap !== 'undefined') {
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
});