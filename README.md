<pagination-template #p="paginationApi" (pageChange)="pageChangeForTable1($event)">
  <!-- Pagination controls and options for table 1 -->
  <select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1(($event.target as HTMLSelectElement).value)">
    <ng-container *ngFor="let item of createRangeForTable1(p.getLastPage())">
      <option [value]="item.value">{{ item.label }}</option>
    </ng-container>
  </select>
</pagination-template>
NG5002: Parser Error: Missing expected ) at column 36 in [pageChangeForTable1(($event.target as HTMLSelectElement).value)] in D:/IT_Portal/IT-Portal/IT-Portal.UI/src/app/change-request/change-request.component.html
