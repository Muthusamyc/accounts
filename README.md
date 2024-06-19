<div class="table-wrapper p-3">
  <table class="fl-table" style="width:100%;margin-left:-1%">
    <thead *ngIf="ischangeanalyst" class="table-head">

      <tr class="border-bottom">
        <th style="width:5%">Select</th>
        <th style="width:5%">Update</th>
        <th style="width:5%">Delete</th>
        <th style="width:10%">RFC #</th>
        <th style="width:10%">Requestor</th>
        <th style="width:20%">Description</th>
        <th style="width:10%">Stage</th>
        <th style="width:10%">RFC Status</th>
        <th style="width:5%">Type</th>
        <th style="width:5%">Classifications</th>
        <th style="width:5%">RFC Date</th>
        <th style="width:5%">Expected Date of Completion</th>
        <th style="width:5%">Task Count</th>
        <!--<th>Attachments</th>-->
      </tr>
    </thead>
    <tbody *ngIf="ischangeanalyst && paginatedTableData.length > 0; else noData">
      <tr class="tr-body" *ngFor="let pltdata of paginatedTableData">
        <td><input type="radio" (click)="onRadioSelect(pltdata)" name="one" id="one" /></td>
        <td>
          <a href="" *ngIf="pltdata.status!='Cancelled'" (click)="onRadio(pltdata)" routerLink="/executive/{{pltdata.itcrid}}/edit">
            <i class="fa fa-pencil-square-o" aria-hidden="true"></i>
          </a>
        </td>
        <td>
          <i *ngIf="pltdata.status!='Cancelled'  && pltdata.status=='Draft'" class="fa fa-trash" aria-hidden="true" (click)="deleteRow(pltdata.itcrid)"></i>
        </td>
        <td>{{pltdata.crcode}}</td>
        <td>{{pltdata.crowner}}</td>
        <td>{{pltdata.changeDesc}}</td>
        <td>{{pltdata.stage}}</td>
        <td [ngSwitch]="pltdata.status.trim()">
          <span *ngSwitchCase="'Draft'"> <span style="color: #3c8dbc;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Pending Approval'"> <span style="color: #808080ff; ">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Submitted'"> <span style="color: rgba(var(--bs-danger-rgb), var(--bs-text-opacity)) !important;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Approved'"> <span style="color: green;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Approved level1'"> <span style="color: green;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Approved level2'"> <span style="color: green;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Completed'"> <span style="color: green;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Rejected'"> <span style="color: red;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Seek Clarification'"> <span style="color:cornflowerblue;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Implement'"> <span class=" text-info">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Implemented'"> <span class=" text-info">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Pending'"> <span style="color: rgba(var(--bs-warning-rgb), var(--bs-text-opacity)) !important;">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Released'"> <span style="color: rgb(154, 235, 73);">{{ pltdata.status }}</span></span>
          <span *ngSwitchCase="'Cancelled'"> <span style="color: rgb(255, 0, 0);">{{ pltdata.status }}</span></span>
        </td>
        <td>{{pltdata.categoryName}}</td>
        <td>{{pltdata.classificationName}}</td>
        <td>{{pltdata.crdate | date:'dd-MM-yyyy' }}</td>
        <td>{{pltdata.estimatedDateCompletion | date:'dd-MM-yyyy' }}</td>
        <td>{{pltdata.taskcount}}</td>
        <!--<td><i class="fa fa-download" aria-hidden="true"></i></td>-->

      </tr>

    </tbody>
    <ng-template #noData>
      <tr *ngIf="ischangeanalyst">
        <td colspan="13">There are no RFCs</td>
      </tr>
    </ng-template>
  </table>



</div>

<mat-paginator [length]="totalItems"
               [pageSize]="pageSize"
               [pageIndex]="pageIndex"
               [pageSizeOptions]="[5, 10, 25, 100]"
               (page)="onPageChange($event)"
               aria-label="Select page" style="margin-right:34%">
</mat-paginator>
above ny html and below my ts:
paginatedTableData: any[] = [];
pageIndex = 0;
pageSize = 10;
totalItems = 1000;

onPageChange(event: PageEvent) {
  this.pageIndex = event.pageIndex;
  this.pageSize = event.pageSize;
  console.log("Page",this.pageSize)
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
      this.crfilter = response.filter((item: any) => item.changeRequestor === parseInt(this.supportid));
      this.filtersdata = this.parseAndSortResponse(this.crfilter);
      this.totalItems = this.crfilter.length;
      const startIndex = this.pageIndex * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      this.paginatedTableData = this.crfilter.slice(startIndex, endIndex);

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

Here when im clicking on the pageIndex, why its not showing the values in the dropdown like 5,10 or more. Nothing is happening after clicking on it. No dropdowns are coming after clicking on it. How to fix that?
