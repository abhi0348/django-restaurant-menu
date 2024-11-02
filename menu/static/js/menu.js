$(document).ready(function () {
    // Add smooth scrolling to all links
    $("a").on("click", function (event) {
        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
            // Prevent default anchor click behavior
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            $("html, body").animate(
                {
                    scrollTop: $(hash).offset().top,
                },
                800,
                function () {
                    // Add hash (#) to URL when done scrolling
                    window.location.hash = hash;
                }
            );
        } // End if
    });

    // Dropdown toggle functionality
    $(".dropdown-toggle").on("click", function (event) {
        event.preventDefault(); // Prevent default link behavior
        $(this).next(".dropdown-menu").toggle(); // Toggle the dropdown menu display
    });

    // Close dropdown if clicking outside of it
    $(document).on("click", function (event) {
        if (!$(event.target).closest(".dropdown").length) {
            $(".dropdown-menu").hide(); // Hide the dropdown menu
        }
    });
});
