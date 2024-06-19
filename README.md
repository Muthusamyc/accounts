<pagination-template #p="paginationApi" (pageChange)="pageChangeForTable1($event)">
  <!-- Pagination controls and options for table 1 -->
  <select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1($event.target.value)">
    <ng-container *ngFor="let item of createRangeForTable1(p.getLastPage())">
      <option [value]="item.value">{{ item.label }}</option>
    </ng-container>
  </select>
</pagination-template>
it showing this error :
NG9: Property 'value' does not exist on type 'EventTarget'.
