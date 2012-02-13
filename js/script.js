/* Author: Todd Foster
Begun 12 Feb 2012
*/

/* global boidem */
boidem = {};

boidem.bcp = (function() {
  var currentPage=0,
  maxPage=996; 

  var pageNumberSelector = (function(n) {
    return '#page' + n;
  });

  var navigateLeftClicked = (function() {
    if (currentPage > 0) {
      $(pageNumberSelector(currentPage)).hide();
      currentPage -= 1;
      $(pageNumberSelector(currentPage)).show();
      $('#navigationInfo').html('Page ' + currentPage + '/' + maxPage);
    }
  });

  var navigateRightClicked = (function() {
    if (currentPage < maxPage) {
      $(pageNumberSelector(currentPage)).hide();
      currentPage += 1;
      $(pageNumberSelector(currentPage)).show();
      $('#navigationInfo').html('Page ' + currentPage + '/' + maxPage);
    }
  });

  return {
    onDocumentReady:function() {
      $('div.bcp_page').hide();
      $(pageNumberSelector(currentPage)).show();
      $('#navigationInfo').html('Page ' + currentPage + '/' + maxPage);

      $('#navigateLeft').click(navigateLeftClicked);
      $('#navigateRight').click(navigateRightClicked);

      // TODO get maxPage from DOM (using jquery's last function)
    }
  }
}());

$(document).ready(boidem.bcp.onDocumentReady);

