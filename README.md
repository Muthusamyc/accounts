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
         <!--<th>Attachments</th>-->          </tr>
     </thead>
     <tbody *ngIf="ischangeanalyst && filtersdata.length > 0; else noData">
       <tr class="tr-body" *ngFor="let pltdata of filtersdata | paginate:{itemsPerPage:noOfRows,currentPage:pagesize }">
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
 <!-- Pagination-->
 <div class="pagination" style="display:flex;justify-content:center;">
   <!--<pagination-controls (pageChange)="page = $event"></pagination-controls>-->

   <tr class="pagination-row">
     <td colspan="3">
       <!-- First Table Pagination -->
       <pagination-template #p="paginationApi" (pageChange)="pageChangeForTable1($event)">
         <!-- Pagination controls and options for table 1 -->
         <select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1($event.target ? ($event.target as HTMLSelectElement).value : null)">
           <ng-container *ngFor="let item of createRangeForTable1(p.getLastPage())">
             <option [value]="item.value">{{ item.label }}</option>
           </ng-container>
         </select>
       </pagination-template>


     </td>
   </tr>
   <pagination-controls (pageChange)="pagesize = $event"></pagination-controls>
 </div>
 <!--Pagination-->
 above my html and below my ts:
 pageChangeForTable1(value: any) {
  if (value !== null && value !== undefined) {
    this.pagesize = Number(value); 
  }
}
  createRangeForTable1(lastPage: number): any {
   
   let pageArray: any = [];
   for (let i = 0; i < lastPage; i++) {
     const page = {
       label: `${i + 1}`,
       value: i + 1
     };
     pageArray.push(page);
   }
   return pageArray;
 }
this for error :
NG5002: Parser Error: Conditional expression $event.target ? ($event.target as HTMLSelectElement requires all 3 expressions at column 72 in [pageChangeForTable1($event.target ? ($event.target as HTMLSelectElement).value : null)]
