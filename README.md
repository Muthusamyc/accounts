 <mat-paginator [length]="totalItems"
                [pageSize]="pageSize"
                [pageIndex]="pageIndex"
                [pageSizeOptions]="[5, 10, 25, 100]"
                (page)="onPageChange($event)"
                aria-label="Select page">
 </mat-paginator>


   paginatedTableData: any[] = [];
  pageIndex = 0;
  pageSize = 10;
  totalItems = 0;

  onPageChange(event: PageEvent) {
    this.pageIndex = event.pageIndex;
    this.pageSize = event.pageSize;
    this.getviewcrdata();
  }

  getviewcrdata() {
    //
    const apiUrls = this.apiurl + '/ViewChangeRequest/ViewChangerequest';
    const requestBody = {}; // You can include request body if needed
    const httpOptions = {
      headers: new HttpHeaders({
        'content-Type': 'application/json'
      })
    };

    this.http.get(apiUrls).subscribe(
      (response: any) => {
        console.log('New:', this.supportid, response);
        // Parse and sort the response before assigning it to viewchangerequest
        /**/
        this.crfilter = response.filter((item: any) => item.changeRequestor === parseInt(this.supportid));
        this.filtersdata = this.parseAndSortResponse(this.crfilter);
        this.paginatedTableData = this.crfilter.slice(this.pageIndex * this.pageSize, (this.pageIndex + 1) * this.pageSize);

        console.log("check support", this.crfilter);
        /*this.tablevalueshow = false;
        this.function();*/
        return this.crfilter
      },
      (error) => {
        console.error("Get failed", error);
      }
    );
  }

this code is not working
