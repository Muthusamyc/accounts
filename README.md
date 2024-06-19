<div class="table-wrapper p-3">
  <table class="fl-table" style="width:100%;margin-left:-1%">
    <!-- Table Header -->
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
      </tr>
    </thead>
    <!-- Table Body -->
    <tbody *ngIf="ischangeanalyst && filtersdata.length > 0; else noData">
      <tr class="tr-body" *ngFor="let pltdata of filtersdata | paginate:{ itemsPerPage: noOfRows, currentPage: pagesize }">
        <td><input type="radio" (click)="onRadioSelect(pltdata)" name="one" id="one" /></td>
        <td>
          <a href="" *ngIf="pltdata.status !== 'Cancelled'" (click)="onRadio(pltdata)" routerLink="/executive/{{ pltdata.itcrid }}/edit">
            <i class="fa fa-pencil-square-o" aria-hidden="true"></i>
          </a>
        </td>
        <td>
          <i *ngIf="pltdata.status !== 'Cancelled' && pltdata.status === 'Draft'" class="fa fa-trash" aria-hidden="true" (click)="deleteRow(pltdata.itcrid)"></i>
        </td>
        <td>{{ pltdata.crcode }}</td>
        <td>{{ pltdata.crowner }}</td>
        <td>{{ pltdata.changeDesc }}</td>
        <td>{{ pltdata.stage }}</td>
        <td [ngSwitch]="pltdata.status.trim()">
          <!-- ngSwitch Cases for different status colors -->
        </td>
        <td>{{ pltdata.categoryName }}</td>
        <td>{{ pltdata.classificationName }}</td>
        <td>{{ pltdata.crdate | date:'dd-MM-yyyy' }}</td>
        <td>{{ pltdata.estimatedDateCompletion | date:'dd-MM-yyyy' }}</td>
        <td>{{ pltdata.taskcount }}</td>
      </tr>
    </tbody>
    <!-- No Data Template -->
    <ng-template #noData>
      <tr *ngIf="ischangeanalyst">
        <td colspan="13">There are no RFCs</td>
      </tr>
    </ng-template>
  </table>

  <!-- Pagination Section -->
  <div class="pagination" style="display:flex;justify-content:center;">
    <pagination-template #p="paginationApi" (pageChange)="pageChangeForTable1($event)">
      <select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1($event.target.value)">
        <ng-container *ngFor="let item of createRangeForTable1(p.getLastPage())">
          <option [value]="item.value">{{ item.label }}</option>
        </ng-container>
      </select>
    </pagination-template>
  </div>
</div>
