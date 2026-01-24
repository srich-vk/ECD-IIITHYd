`timescale 1ns/1ps
`include "alu.v"

module alu_64_bit_tb;
    reg [63:0] a, b;
    reg [3:0] opcode;
    wire [63:0] result;
    wire cout, carry_flag, overflow_flag, zero_flag;
    integer pass_count = 0, total_tests = 2;
    
    // Control codes
    localparam  ADD_Oper  = 4'b0000,
                SLL_Oper  = 4'b0001,
                SLT_Oper  = 4'b0010,
                SLTU_Oper = 4'b0011,
                XOR_Oper  = 4'b0100,
                SRL_Oper  = 4'b0101,
                OR_Oper   = 4'b0110,
                AND_Oper  = 4'b0111,
                SUB_Oper  = 4'b1000,
                SRA_Oper  = 4'b1101;
    
    // Instantiate the ALU wrapper
    alu_64_bit uut(
        .a(a),
        .b(b),
        .opcode(opcode),
        .result(result),
        .cout(cout),
        .carry_flag(carry_flag),
        .overflow_flag(overflow_flag),
        .zero_flag(zero_flag)
    );

    task run_test;
        input [4:0] test_number;
        input [63:0] test_a, test_b, expected_result;
        input [3:0] test_opcode;
        input exp_carry, exp_overflow, exp_zero;
        begin
            a = test_a;
            b = test_b;
            opcode = test_opcode;
            #10;
            $display("Test %d:", test_number);
            $display("A: %016h", a);
            $display("B: %016h", b);
            $display("Opcode: %b", test_opcode);
            $display("Result: %016h", result);
            $display("Flags: C=%b, O=%b, Z=%b", carry_flag, overflow_flag, zero_flag);
            
            if (result === expected_result && 
                carry_flag === exp_carry && 
                overflow_flag === exp_overflow && 
                zero_flag === exp_zero) begin
                pass_count = pass_count + 1;
                $fdisplay(file_handle, "Test %0d, Status: PASS", test_number);
            end else begin
                $fdisplay(file_handle, "Test %0d, Status: FAIL", test_number);
                $display("Expected: result=%016h, carry=%b, overflow=%b, zero=%b", 
                        expected_result, exp_carry, exp_overflow, exp_zero);
                $display("Got:      result=%016h, carry=%b, overflow=%b, zero=%b\n", 
                        result, carry_flag, overflow_flag, zero_flag);
            end
        end
    endtask

    integer file_handle;

    initial begin
        file_handle = $fopen("alu_results.txt", "w");

        // Check if file opened successfully
        if (file_handle == 0) begin
            $display("Error: Could not open file for writing.");
            $finish;
        end
        $dumpfile("alu_tb.vcd");
        $dumpvars(0, alu_64_bit_tb);

        pass_count = 0;

        // Test cases
        run_test(1, 64'h7FFFFFFFFFFFFFFF, 64'h0000000000000001, 64'h8000000000000000, ADD_Oper, 0, 1, 0);
        run_test(2, 64'hFFFF0000FFFF0000, 64'h00000000FFFF0000, 64'hFFFF0000FFFF0000, OR_Oper, 0, 0, 0);
    
        $display("Passed %0d/%0d tests", pass_count, total_tests);
        $fdisplay(file_handle, "Passed %0d/%0d tests", pass_count, total_tests);
        #10 $finish;
    end
endmodule