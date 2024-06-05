document.addEventListener("DOMContentLoaded", function () {
  const approveButtons = document.querySelectorAll(".approve-btn");
  const deleteButtons = document.querySelectorAll(".delete-btn");
  const editButtons = document.querySelectorAll(".edit-btn");
  const formSubmitBtn = document.querySelector("#form-submit-btn");
  const formCommentField = document.querySelector("#id_comment");


  /**
   * Check if we need to restore the scroll position which will always
   * be the case if the user has clicked any of the CRUD buttons
   * after HttpResponseRedirect has ben executed in the view.
   * It will not be the case when the page is first loaded as there
   * won't be any scroll position captured, that only happens
   * when a CRUD button is clicked.
   *
   * Clear the scrollPosition so that it won't be reused
   * every time the page is loaded.
   */
  const scrollPosition = localStorage.getItem("scrollPosition");
  if (scrollPosition) {
    window.scrollTo(0, parseInt(scrollPosition));
    localStorage.removeItem("scrollPosition");
  }


  // Approve button functionality
  approveButtons.forEach(button => {
    /**
     * Given the button clicked is linked to a valid comment id
     * store the current scroll position so that it can be
     * restored when the user is returned to the event page.
     *
     * Redirect to approve_comment view where HttpResponseRedirect will be
     * executed after the comment approval has been attempted to return the user
     * to the previous page, ie the event page where the comment was made.
     *
     * Add class "disabled" after clicking to prevent excessive request spam.
     */
    $(button).click((e) => {
      const commentId = e.target.dataset.target_comment;

      if (commentId) {
        localStorage.setItem("scrollPosition", window.scrollY);
        $(button).addClass("disabled");
        window.location.href = `approve_comment/${commentId}`;
      } else {
        alert("Comment ID not found.");
      }
    });
  });


  // Delete button functionality
  deleteButtons.forEach(button => {
    /**
     * Given the button clicked is linked to a valid comment id
     * store the current scroll position so that it can be
     * restored when the user is returned to the event page.
     *
     * Redirect to delete_comment view where HttpResponseRedirect will be
     * executed after the comment deletion has been attempted to return the user
     * to the previous page, ie the event page where the comment was made.
     *
     * Add class "disabled" after confirming to prevent excessive request spam,
     * which would lead to a 404 error.
     */
    $(button).click((e) => {
      const commentId = e.target.dataset.target_comment;

      if (commentId) {
        localStorage.setItem("scrollPosition", window.scrollY);
        $("#confirm-delete").click(() => {
          $("#confirm-delete").addClass("disabled");
          window.location.href = `delete_comment/${commentId}`;
        });
      } else {
        alert("Comment ID not found.");
      }
    });
  });


  $(formSubmitBtn).click(() => {
    /**
     * Capture scroll position when form is submitted so
     * scroll level can be restored once comment is posted.
     * 
     * Disable the button if there's any content in the form
     * to POST to stay consistent with the other button
     * behaviors.
     */
    localStorage.setItem("scrollPosition", window.scrollY);
    if (formCommentField.value !== "") {
      $(formSubmitBtn).addClass("disabled");
    }
  });


  // Edit button functionality
  editButtons.forEach(button => {
    /**
     * When an edit button is clicked the comment id and the
     * comments html structure as well as text are saved to
     * feed the edit togglers with the original comment content.
     *
     * Call $(button).off(); after the initial click event to
     * avoid duplicate execution on the same comment.
     *
     * Call editComment to start the editing and change the button
     * edit button content, then add a new click event listener to
     * initiate toggling between editing, and the original comment
     * if the user chooses to abandon editing the comment.
     *
     * Every time the toggler is clicked the button's content
     * and class is updated to update the togglers state and
     * to inform the user of the state.
     */
    $(button).click((e) => {
      const commentId = e.target.dataset.target_comment;
      const commentHtml = $(`#comment${commentId}`).html();
      const commentText = $(`#comment${commentId}`).text();
      $(button).off();

      if (commentId) {
        button.innerHTML = "Cancel";
        button.classList.replace("edit-btn", "close-edit-btn");
        editComment(commentId, commentText);

        $(button).click(() => {
          if (button.innerHTML == "Edit") {
            button.innerHTML = "Cancel";
            button.classList.replace("edit-btn", "close-edit-btn");
            editComment(commentId, commentText);
          } else if (button.innerHTML == "Cancel") {
            button.innerHTML = "Edit";
            button.classList.replace("close-edit-btn", "edit-btn");
            restoreComment(commentId, commentHtml);
          }
        });
      } else {
        alert("Comment ID not found.");
      }
    });
  });

  /**
   * Function to switch a comment to edit mode if the
   * user clicked the edit button.
   *
   * Store the users scroll position after clicking edit
   * to restore the user back to same position after
   * submission.
   *
   * Replace the comment's HTML with an edit form to handle
   * the POST request, with the orignal comment text in the
   * textarea for the user to start editing from (csrftoken is
   * defined in the template using DTL).
   *
   * Disable the save button after it is clicked to prevent
   * multiple submission requests.
   *
   * @param commentId - The ID of the comment to be edited.
   * @param commentText - The original text content of the comment.
   */
  function editComment(commentId, commentText) {
    localStorage.setItem("scrollPosition", window.scrollY);

    $(`#comment${commentId}`).html(`
    <form method="post" action="edit_comment/${commentId}">
      <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
      <label for="id_comment">Edit comment:</label>
      <textarea name="comment" class="form-control" required="" id="id_comment"
       style="height: 20vh;">${commentText}</textarea>
      <input class="btn edit-btn mt-3" type="submit" id="saveComment"
       value="Save">
    </form>
  `);

    // Ensure the comment is fully visible if it is unapporved while editing
    if ($(`#comment${commentId}`).hasClass("opacity-50")) {
      $(`#comment${commentId}`).addClass("opacity-100").removeClass("opacity-50");
    }

    $("#saveComment").click(() => {
      $("#saveComment").addClass("disabled");
    });
  }

  /**
   * Function to restore the original comment content if
   * the user chooses to abandon editing.
   *
   * Remove the stored scroll position as it will not be needed
   * if the user canceled editing since no redirection will take place.
   *
   * Restore the comment back to it's saved original state.
   *
   * If the comment is unapproved restore the opacity too.
   *
   * @param commentId - The ID of the comment to be restored.
   * @param commentHtml - The original HTML content of the comment.
   */
  function restoreComment(commentId, commentHtml) {
    localStorage.removeItem("scrollPosition");

    $(`#comment${commentId}`).html(commentHtml);

    // Restore the comments opacity if it is unapproved
    if ($(`#comment${commentId}`).hasClass("opacity-100")) {
      $(`#comment${commentId}`).addClass("opacity-50").removeClass("opacity-100");
    }
  }

});