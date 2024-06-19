<select name="pageToggle" id="pageToggle" [(ngModel)]="pagesize" (change)="pageChangeForTable1($event?.target?.value)">
  <ng-container *ngFor="let item of createRangeForTable1(p?.getLastPage() ?? 0)">
    <option [value]="item.value">{{ item.label }}</option>
  </ng-container>
</select>
