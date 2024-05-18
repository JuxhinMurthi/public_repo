/** @odoo-module */
import { KanbanController } from "@web/views/kanban/kanban_controller";
import { registry } from '@web/core/registry';
import { kanbanView } from '@web/views/kanban/kanban_view';
export class ProductKanbanController extends KanbanController {
   setup() {
       super.setup();
   }

    OnTestClick() {
        this.actionService.doAction('tech_gear_inventory.action_product_template_xlsx_wizard');
    }
}
registry.category("views").add("button_in_kanban", {
   ...kanbanView,
   Controller: ProductKanbanController,
   buttonTemplate: "button_product_kanban.KanbanView.Buttons",
});