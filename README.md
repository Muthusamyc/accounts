import { HttpClient, HttpHeaders } from '@angular/common/http';

constructor(private http: HttpClient) {}

getviewcrdata() {
  const apiUrls = this.apiurl + '/ViewChangeRequest/ViewChangerequest';

  this.http.get(apiUrls).subscribe(
    (response: any) => {
      console.log('API Response:', response);

      // Assuming response is an array of data
      this.crfilter = response.filter((item: any) => item.changeRequestor === parseInt(this.supportid));
      this.filtersdata = this.parseAndSortResponse(this.crfilter);

      // Update paginatedTableData based on current pageIndex and pageSize
      const startIndex = this.pageIndex * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      this.paginatedTableData = this.crfilter.slice(startIndex, endIndex);

      console.log("Filtered Data:", this.crfilter);
    },
    (error) => {
      console.error("API Error:", error);
    }
  );
}

parseAndSortResponse(data: any[]): any[] {
  // Implement your parsing and sorting logic here if needed
  return data; // Placeholder, modify as per your requirement
}
